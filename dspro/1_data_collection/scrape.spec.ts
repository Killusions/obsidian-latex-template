import { test, ElementHandle } from '@playwright/test';
import fs from 'fs';
import 'dotenv/config';
import { Page } from 'playwright-core';
import { describe } from 'node:test';
import { MAX_MINUTES, NUMBER_OF_INSTANCES, getTimestampString } from './playwright_base_config';
import checkDiskSpace from 'check-disk-space';
import path from 'path';

let logProgressInterval: ReturnType<typeof setInterval> | undefined;

const error = (message: string, i?: string) => {
  console.error((i ? i + ' - ' : '') + message);
};

let progressLogDisabled = false;

// Log a message, print a dot (on the same line) every 10 seconds in a background process to get progress indication until another message is logged
const log = (message: string, i?: string) => {
  console.log((i ? i + ' - ' : '') + message);
  if (!i) {
    if (logProgressInterval) {
      clearInterval(logProgressInterval);
    }
    logProgressInterval = setInterval(() => (!progressLogDisabled ? process.stdout.write('.') : undefined), 10000);
  }
};

const getVolumeRoot = (currentPath: string) => {
  if (process.platform === 'win32') {
    // Get the drive letter and append ':\'
    return currentPath.split(path.sep)[0] + '\\';
  } else {
    return '/';
  }
};

const hasEnoughFreeDiskSpace = async () => {
  const cwd = process.cwd();

  const volumeRoot = getVolumeRoot(cwd);

  const diskSpace = await checkDiskSpace(volumeRoot);

  // Is there more free storage than 100MB in bytes
  return diskSpace.free > 100 * 1024 * 1024;
};

const waitForFreeDiskSpace = async (identifier?: string) => {
  let first = true;
  while (!(await hasEnoughFreeDiskSpace())) {
    if (first) {
      log('Waiting for free disk space', identifier);
    }
    first = false;
    await new Promise((resolve) => setTimeout(resolve, 1000));
  }
};

const getButtonWithText = (page: Page, text: string, only = false) => {
  return page.locator('button, a').getByText(text, { exact: only });
};

const clickButtonWithText = async (page: Page, text: string, wait = 0, only = false) => {
  const button = getButtonWithText(page, text, only);
  if (wait) {
    await button.waitFor({ state: 'visible', timeout: wait !== -1 ? wait : undefined });
  }
  return await button.click();
};

const clickButtonIfFound = async (page: Page, text: string, only = false, first = false, last = false, noWaitAfter = false) => {
  let button = getButtonWithText(page, text, only);
  if (first) {
    button = button.first();
  }
  if (last) {
    button = button.last();
  }
  if ((await button.count()) > 0) {
    await button.click({ noWaitAfter });
    return true;
  }
  return false;
};

const setCookies = async (page: Page, path: string) => {
  // File could be undefined, so check if it exists, but keep synchronous
  if (fs.existsSync(path + 'cookies.json')) {
    const cookies = JSON.parse(fs.readFileSync(path + 'cookies.json', 'utf8'));
    await page.context().addCookies(cookies);
  }
};

// Inject css with a way to remove it again
const injectCss = async (page: Page, css: string) => {
  return await page.addStyleTag({ content: css });
};

const removeElement = async (element: ElementHandle<Node>) => {
  return await element.evaluate((el) => el.parentNode?.removeChild(el));
};

// Random 10 character UUID
const randomUUID = () => {
  return 'xxxxxxxxxx'.replace(/x/g, () => Math.floor(Math.random() * 16).toString(16));
};

describe('Scraping', () => {
  for (let i = 0; i < NUMBER_OF_INSTANCES; i++) {
    const identifier = NUMBER_OF_INSTANCES > 1 ? String(i + 1) : '';

    test('scrape' + (identifier ? ' - ' + identifier : ''), async ({ page }) => {
      try {
        test.setTimeout(60000 * MAX_MINUTES);
        // TODO: Add scraping here
        await Promise.resolve();
      } catch (e: unknown) {
        const timestamp = getTimestampString();
        // If messages includes 'Target crashed', exit program, otherwise log an error message that an Error occurred in this instance at this time and rethrow
        if (typeof e === 'object' && e instanceof Error && (e.message.includes('Target crashed') || e.message.includes('exited unexpectedly'))) {
          error(`Crash occurred at ${timestamp}, stopping:`, identifier);
          console.error(e);
          process.exit(1);
        } else {
          error(`Error occurred at ${timestamp}:`, identifier);
          console.error(e);
          throw e;
        }
      }
    });
  }
});

export const MAX_MINUTES = process.env.CI ? 60 * 24 * 14 : 60;
export const MAX_RETRIES = process.env.CI ? 10000 : 0;
export const NUMBER_OF_INSTANCES = process.env.CI ? 5 : 1;
export const getTimestampString = () => new Date().toISOString().replace(/[:.]/g, '-');

import { getTimestampString } from './playwright_base_config.js';

const timestamp = getTimestampString();

console.log('Setting up environment...');
// Create required directories and files here
console.log('Set up at ' + timestamp);

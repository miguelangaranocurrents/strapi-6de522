// The record key stays out of this object: tests/scripts/run-tests.js serializes the
// Playwright config (reporter options included) and the JSON report copies it. The
// reporter reads CURRENTS_RECORD_KEY from the environment.
/** @type {Partial<import('@currents/playwright').CurrentsConfig>} */
const config = {
  projectId: process.env.CURRENTS_PROJECT_ID,
  consoleOutput: 'compact',
  contextLinks: true,
  outputFile: 'currents-report.json',
};

module.exports = config;

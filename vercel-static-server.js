// vercel-static-server.js
const { createServer } = require('http');
const { join } = require('path');
const { parse } = require('url');
const next = require('next');

const dev = false;
const app = next({ dev });
const handle = app.getRequestHandler();

module.exports = createServer((req, res) => {
  const parsedUrl = parse(req.url, true);
  const { pathname } = parsedUrl;

  // Serve static files directly
  if (pathname.startsWith('/static/')) {
    const filePath = join(__dirname, 'staticfiles', pathname.replace('/static/', ''));
    return require('serve-handler')(req, res, {
      public: 'staticfiles',
      cleanUrls: false,
      headers: [{
        source: '**/*',
        headers: [{
          key: 'Cache-Control',
          value: 'public, max-age=31536000, immutable'
        }]
      }]
    });
  }

  return handle(req, res, parsedUrl);
});
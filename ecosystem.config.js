module.exports = {
  apps: [{
    name: 'gabriel-merrin-website',
    script: './hugo',
    args: 'server --bind 0.0.0.0 --port 1313 --disableFastRender',
    cwd: '/home/user/webapp',
    instances: 1,
    autorestart: true,
    watch: false,
    max_memory_restart: '1G',
    env: {
      NODE_ENV: 'development',
      HUGO_ENV: 'development'
    },
    error_file: './logs/err.log',
    out_file: './logs/out.log',
    log_file: './logs/combined.log',
    time: true
  }]
};
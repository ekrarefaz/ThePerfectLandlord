const { defineConfig } = require('@vue/cli-service')
const path = require('path');

module.exports = {
    proxy: 'http://127.0.0.1',
    filenameHashing: false, // Django will hash file names, not webpack
    runtimeCompiler: true, // See: https://vuejs.org/v2/guide/installation.html#Runtime-Compiler-vs-Runtime-only
    devServer: {
      devMiddleware:{
        writeToDisk: true, // Write files to disk in dev mode, so Django can serve the assets
      }
    },
};


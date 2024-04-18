import 'dotenv/config'
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default () => {

  // process.env = {...process.env, ...loadEnv(mode, process.cwd())};

  console.log('api url:', process.env.API_URL)

  return defineConfig({
    plugins: [react()],
    server: {
      proxy: {
        '/api': process.env.API_URL || 'http://localhost:5000',
      },
    },
    build: {
      outDir: '../server/static'
    }
  })
}



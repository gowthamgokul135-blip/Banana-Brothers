

export default defineConfig({
  plugins: [react()],

  base: "/Banana-Brothers/",

  server: {
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true
      }
    }
  }
});
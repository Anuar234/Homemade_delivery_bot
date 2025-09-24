import { createApp } from 'vue'
import App from './App.vue'
import { init } from '@telegram-apps/sdk-vue'

// Инициализация Telegram Web App
init()

createApp(App).mount('#app')
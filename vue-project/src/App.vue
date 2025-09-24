<template>
  <div class="app">
    <h1>Telegram Mini App</h1>
    <p>User ID: {{ telegramUser?.id }}</p>
    <button @click="sendData">Отправить данные</button>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useWebApp } from '@telegram-apps/sdk-vue'

const webApp = useWebApp()
const telegramUser = ref(null)

onMounted(() => {
  webApp.ready()
  telegramUser.value = webApp.initDataUnsafe.user
})

const sendData = () => {
  webApp.sendData(JSON.stringify({ action: 'test' }))
}
</script>
<script setup>
import { RouterLink } from 'vue-router';
defineProps({
  msg: {
    type: String,
    default: 'Sorry, the page you are looking for does not exist.'
  },
  error: {
    type: String,
    default: '404 Not Found'
  }
})
</script>

<template>
    <section class="text-center flex flex-col justify-center items-center h-96">
      <i class="pi pi-exclamation-triangle animate-bounce text-yellow-500 text-7xl mb-5"></i>
      <h1 class="text-6xl font-bold dark:text-white mb-4">{{ error }}</h1>
      <p class="text-xl mb-5 dark:text-white">{{ msg }}</p>
      <RouterLink
        to="/"
        class="text-white bg-green-700 animate-pulse hover:bg-green-900 rounded-md px-3 py-2 mt-4"
        >Go Back</RouterLink
      >
    </section>
</template>
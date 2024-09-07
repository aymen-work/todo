<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Navbar from './components/navbar.vue'
</script>

<template>
  <main class=" bg-white dark:bg-slate-900 h-screen">
    <Navbar/>

    <RouterView/>
  </main>
  
</template>

<style scoped>
</style>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Navbar from './components/navbar.vue'
</script>

<template>
  <main class=" bg-white dark:bg-slate-900 h-screen">
    <Navbar/>
    <transition name="app">
      <RouterView/>

    </transition>
  </main>
  
</template>

<style scoped>
.app-enter-from{
  opacity: 0;
  /* transform: scale(0.5); */
  /* transform: translateX(-100%); */
}
.app-enter-to{
  opacity: 5;
  /* transform: scale(1); */
  /* transform: translateX(0); */
}
.app-enter-active{
  transition:all 1.0s ease
}
</style>

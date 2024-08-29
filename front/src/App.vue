<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Navbar from './components/navbar.vue'
import HomeView from './views/HomeView.vue';
</script>

<template>
  <Navbar/>
  
  <RouterView/>
</template>

<style scoped>
</style>

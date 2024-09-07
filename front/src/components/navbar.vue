<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useDark, useToggle } from "@vueuse/core";
import { useRoute } from 'vue-router';
import { onMounted } from 'vue';

const isDark = useDark();
const toggleDark = useToggle(isDark);
const route = useRoute()
</script>

<template>
  <nav class="bg-green-700 dark:bg-slate-900 border-b border-green-500">
    <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
      <div class="flex h-20 items-center justify-between">
        <div class="flex flex-1 items-center justify-center md:items-stretch md:justify-start">
          <!-- Logo -->
          <a class="flex flex-shrink-0 items-center mr-4" href="index.html">
            <i class="pi pi-pen-to-square" style="font-size: 2.5rem; color: white"></i>
            <span class="hidden md:block text-white text-2xl font-bold ml-2">Tasks</span>
          </a>
          <div class="md:ml-auto">
            <div class="flex space-x-2">
              <RouterLink to="/" :class="['text-white', route.fullPath == '/'?'bg-green-900':null, 'hover:bg-gray-900', 'dark:hover:bg-green-800', 'hover:text-white', 'rounded-md', 'px-3', 'py-2']">
                Home</RouterLink>
              <RouterLink to="/tasks" :class="['text-white', route.fullPath == '/tasks'?'bg-green-900':null, 'hover:bg-gray-900', 'dark:hover:bg-green-800', 'hover:text-white', 'rounded-md', 'px-3', 'py-2']">All
                Tasks</RouterLink>
              <RouterLink to="/tasks/add" :class="['text-white', route.fullPath == '/tasks/add'?'bg-green-900':null, 'hover:bg-gray-900', 'dark:hover:bg-green-800', 'hover:text-white', 'rounded-md', 'px-3', 'py-2']">Add
                Job</RouterLink>
              <button type="button" @click="toggleDark()"
                class="border dark:border-white  border-black px-2 rounded-full">
                <i id="theme_icon" class="pi pi-moon dark:text-white"></i>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

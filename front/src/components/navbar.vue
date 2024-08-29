<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
    <nav class="bg-blue-500 border-b border-green-500">
      <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
        <div class="flex h-20 items-center justify-between">
          <div
            class="flex flex-1 items-center justify-center md:items-stretch md:justify-start"
          >
            <!-- Logo -->
            <a class="flex flex-shrink-0 items-center mr-4" href="index.html">
                <i class="pi pi-pen-to-square" style="font-size: 2.5rem;color:white"></i>
              <span class="hidden md:block text-white text-2xl font-bold ml-2"
                >Vue Jobs</span
              >
            </a>
            <div class="md:ml-auto">
              <div class="flex space-x-2">
                <RouterLink
                  to="/"
                  class="text-white bg-blue-900 hover:bg-gray-900 hover:text-white rounded-md px-3 py-2"
                  >Home</RouterLink
                >
                <RouterLink
                  to="/tasks"
                  class="text-white hover:bg-blue-900 hover:text-white rounded-md px-3 py-2"
                  >All Tasks</RouterLink
                >
                <RouterLink
                  to="/tasks/add"
                  class="text-white hover:bg-blue-900 hover:text-white rounded-md px-3 py-2"
                  >Add Job</RouterLink
                >
              </div>
            </div>
          </div>
        </div>
      </div>
    </nav>
</template>
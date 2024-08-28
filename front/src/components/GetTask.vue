<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";
import { useToast } from "vue-toastification";

const toast = useToast()
const data = ref()

onMounted(async () => {
    try {
        const response = await axios.get('api/api/v1/tasks')
        console.log('Tasks fetched:', response.data)
        data.value = response.data
        console.log("__⚠️⚠️⚠️__ ~ :", data.value)
        toast.success(`${data.value[0].title}`)
    }catch(error){
        console.error('Error fetching tasks:', error)
        toast.error('Error fetching tasks')
    }
})
</script>

<template>
    <div v-for="t in data"class="grid grid-flow-col mt-5">
        <div class="col-span-1">{{ t.id }}</div>
        <div class="col-span-1">{{ t.title }}</div>
        <div class="col-span-1">{{ t.end_date }}</div>
    </div>
</template>

<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";
import { useToast } from "vue-toastification";
import Alert from "./Alert.vue";

const toast = useToast()
const data = ref()

onMounted(async () => {
    try {
        const response = await axios.get('api/api/v1/tasks')
        console.log('Tasks fetched:', response.data)
        data.value = response.data
    }catch(error){
        console.error('Error fetching tasks:', error)
        toast.error('Error fetching tasks')
    }
})
</script>

<template>
    <div v-if="data" v-for="t in data"class="grid grid-flow-col mt-5">
        <div class="col-span-1">{{ t.id }}</div>
        <div class="col-span-1">{{ t.title }}</div>
        <div class="col-span-1">{{ t.end_date }}</div>
        <div class="col-span-1" v-if="t.status === 'pending'"><i class="pi pi-clock bg-blue-500 rounded-lg"></i></div>
        <div class="col-span-1" v-else-if="t.status === 'completed'"><i class="pi pi-check-square bg-green-500"></i></div>
        <div class="col-span-1" v-else><i class="pi pi-times bg-red-300 rounded border-black border"></i></div>
    </div>
    <Alert class="mt-5" msg="There is problem with getting data from server ,maybe the server is closed" v-else/>
</template>

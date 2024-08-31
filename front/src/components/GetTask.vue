<script setup>
import axios from "axios";
import { onMounted, ref, watch } from "vue";
import { useToast } from "vue-toastification";
import Alert from "./Alert.vue";

const toast = useToast()
const data = ref()
const status = ref('pending')


onMounted(async () => {
    try {
        const response = await axios.get(`api/api/v1/tasks/${status.value}`)
        data.value = response.data
    } catch (error) {
        console.error('Error fetching tasks:', error)
        toast.error('Error fetching tasks')
    }
})

watch(() => status.value, async (newStatus) => {
    const response = await axios.get(`api/api/v1/tasks/${status.value}`)
    data.value = response.data
})

function aa(m){
    if(m.status === 'completed'){
        toast.success('Tasks completed')
    }else if(m.status === 'cancelled'){
        toast.warning('Tasks cancelled')
    }else{
        toast.info(`Tasks pending and expired in ${m.end_date}`)
    }
}

</script>

<template>
    
   
<div class="flex flex-wrap">
    <div class="flex items-center me-4">
        <input @change="status = 'completed'" type="radio" value="" name="colored-radio" class="w-4 h-4 text-red-600 bg-gray-100 border-gray-300 focus:ring-red-500 dark:focus:ring-green-500 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
        <label for="red-radio" class="ms-2 text-sm font-medium text-gray-900">Completed</label>
    </div>
    <div class="flex items-center me-4">
        <input @change="status = 'cancelled'" type="radio" value="" name="colored-radio" class="w-4 h-4 text-green-600 bg-gray-100 border-gray-300 focus:ring-green-500 dark:focus:ring-red-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
        <label for="green-radio" class="ms-2 text-sm font-medium text-gray-900 ">Cancelled</label>
    </div>
    <div class="flex items-center me-4">
        <input checked @change="status = 'pending'" type="radio" value="" name="colored-radio" class="w-4 h-4 text-purple-600 bg-gray-100 border-gray-300 focus:ring-yellow-500 dark:focus:ring-yallow-400 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
        <label for="purple-radio" class="ms-2 text-sm font-medium text-gray-900 ">Pending</label>
    </div>
    
</div>


    <div  v-if="data" v-for="t in data" @click="aa(t)" class="grid grid-flow-col mt-5 hover:cursor-pointer">
        <div class="col-span-1">{{ t.id }}</div>
        <div class="col-span-1">{{ t.title }}</div>
        <div class="col-span-1">{{ t.end_date }}</div>
        <div class="col-span-1" v-if="t.status === 'pending'"><i class="pi pi-clock bg-blue-500 rounded-lg"></i></div>
        <div class="col-span-1" v-else-if="t.status === 'completed'"><i class="pi pi-check-square bg-green-500"></i>
        </div>
        <div class="col-span-1" v-else><i class="pi pi-times bg-red-300 rounded border-black border"></i></div>
    </div>
    <Alert class="mt-5" msg="There is problem with getting data from server ,maybe the server is closed" v-else />
</template>

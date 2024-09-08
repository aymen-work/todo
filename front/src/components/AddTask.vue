<script setup>
import axios from 'axios';
import { onMounted, reactive } from 'vue';
import router from '@/router';
import { useRoute } from 'vue-router';
import { useToast } from 'vue-toastification';
import dayjs from 'dayjs';

const toast = useToast();
const route = useRoute();
defineProps({
    title:{
        default: 'Add task',
        type: String,
    },
})

const form = reactive({
    title: '',
    details: '',
    end_date: '',
})

onMounted(async ()=>{
    if(route.name === 'update'){
        const id = route.params.id
        const result = await axios.get(`/api/api/v2/tasks/${id}`)
        form.title = result.data.title
        form.details = result.data.details
        form.end_date = dayjs(result.data.end_date).format('YYYY-MM-DDTHH:mm')
        // console.log( result.data.end_date.split('T'),dayjs(result.data.end_date).format('YYYY-MM-DDTHH:mm'))
    }
})

const addTask = async () => {
    const data = {
        title: form.title,
        details: form.details,
        end_date: form.end_date,
        status: 'pending', 
    };
    try{
        const response = await axios.post('/api/api/v2/addtask',data)
        router.push('/tasks')
        toast.success('Task was added successfully')
    }catch(error) {
        console.error('Error adding task:', error);
    }
}
const updateTask = async () => {
    try{const id = route.params.id
    const newdata = {
        title: form.title,
        details: form.details,
        end_date: form.end_date,
    };
    const update = await axios.patch(`/api/api/v2/tasks/${id}`,newdata)
    router.push('/tasks')
}
    catch(error) {
        toast.error('Error updating task:', error);
    }
}

</script>

<template>
    <div class="container">
        <div class="rounded-lg text-center p-5  mt-20 w-2/4 mx-auto shadow-lg bg-slate-300 shadow-slate-500">
            <h1 class="font-bold text-3xl underline">{{ title }}</h1>
            <form @submit.prevent="title==='Update'?updateTask() : addTask()" class="max-w-sm mx-auto">
                <div class="mb-5">
                    <label for="title" class="block mb-2 font-medium text-gray-900 text-xl mt-6 ">Your title</label>
                    <input type="title" id="title" v-model="form.title"
                        class="bg-gray-50 dark:bg-slate-500 dark:placeholder-white dark:text-white placeholder-black border border-gray-300 text-gray-900 text-sm rounded-lg block w-full p-2.5 focus:outline-blue-600 "
                        placeholder="Title of task" required />
                </div>
                <div class="mb-5">
                    <label for="details" class="block mb-2 font-medium text-gray-900 text-xl">Your details</label>
                    <textarea id="details" v-model="form.details"
                        class="bg-gray-50 dark:bg-slate-500 dark:placeholder-white dark:text-white placeholder-black border border-gray-300 text-gray-900 text-sm rounded-lg block w-full p-2.5 focus:outline-blue-600"
                        required placeholder="write details of your task here ..."></textarea>
                    <label for="details" class="block mb-2 font-medium text-gray-900 text-xl">End date</label>

                    <input type="datetime-local" class="bg-gray-50 dark:bg-slate-500 dark:placeholder-white placeholder-black border border-gray-300 text-black dark:text-white text-sm rounded-lg block w-full p-2.5 focus:outline-blue-600" placeholder="" v-model="form.end_date">
                </div>

                <button type="submit"
                    class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center ">Submit</button>
            </form>



        </div>
    </div>
</template>
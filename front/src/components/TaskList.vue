<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";
import { useToast } from "vue-toastification";
import Alert from "./Alert.vue";

const toast = useToast();
const data = ref();

onMounted(async () => {
  try {
    const response = await axios.get("api/api/v1/tasks");
    console.log("Tasks fetched:", response.data);
    data.value = response.data;
  } catch (error) {
    console.error("Error fetching tasks:", error);
    toast.error("Error fetching tasks");
  }
});

async function cancelTask(id) {
  try {
    const confirm = window.confirm(
      "Are you sure you want to cancel this task?"
    );
    if (confirm) {
      const response = await axios.patch(`api/api/v2/tasks/${id}`, {
        status: "cancelled",
      });
      window.location.reload();
    }
  } catch (error) {
    console.error("Error canceling task:", error);
    toast.error("Error canceling task");
  }
}

async function deleteTask(id) {
  try{
    const confirm = window.confirm('Are you sure you want to delete this task?')
    if(confirm){
      const response = await axios.delete(`api/api/v2/tasks/${id}`)
      window.location.reload();
    }
  }catch(error){
    console.log("Error deleting task:", error);
    toast.error("Error deleting task");
  }
}

async function doneTask(id) {
  try {
    const confirm = window.confirm(
      "Are you sure you want to cancel this task?"
    );
    if (confirm) {
      const response = await axios.patch(`api/api/v2/tasks/${id}`, {status: "completed",});
      // toast.success("Task marked as done");
      window.location.reload();
    }
  } catch (error) {
    console.error("Error marking task as done:", error);
    toast.error("Error marking task as done");
  }
}
</script>

<template>
  <section class="bg-blue-50 px-4 py-10">
    <div class="container-xl lg:container m-auto">
      <h2 class="text-3xl font-bold text-blue-500 mb-6 text-center">
        Browse Tasks
      </h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <!-- Job Listing 1 -->
        <div v-for="t in data" :class="[
          'border-t-8',
          t.status == 'cancelled'
            ? 'border-red-600'
            : t.status == 'completed'
              ? 'border-green-400'
              : 'border-yellow-400',
          'bg-white',
          'rounded-xl',
          'shadow-md',
          'relative',
        ]">
          <div class="p-4">
            <div class="mb-6 text-center">
              <h3 class="text-xl font-bold">{{ t.title }}</h3>
            </div>

            <div class="mb-5 text-xl">
              {{ t.details }}
            </div>

            <h3 class="text-blue-500 mb-2">Start Date: {{ t.created_date }}</h3>
            <h3 class="text-blue-500 mb-2">Start Date: {{ t.end_date }}</h3>

            <div class="border border-gray-100 mb-5"></div>

            <div class="grid grid-flow-col mb-4">
              <div class="font-bold text-black col-span-4 mb-3">
                <i class="fa-solid fa-location-dot text-lg"></i>
                {{ t.status.toUpperCase() }}
              </div>
              <button v-if="t.status !== 'completed' & t.status !== 'cancelled'" @click="cancelTask(t.id)"
                class="h-[36px] bg-yellow-500 hover:bg-yellow-600 col-span-1 text-white px-4 mr-3 py-2 rounded-lg text-center text-sm">
                Cancel
              </button>
              <button v-if="t.status !== 'completed' & t.status !== 'cancelled'" @click="doneTask(t.id)"
                class="h-[36px] bg-green-500 hover:bg-green-600 col-span-1 text-white px-4 py-2 rounded-lg text-center text-sm">
                Done
              </button>
              <button v-if="t.status === 'completed' | t.status === 'cancelled'" @click="deleteTask(t.id)"
                class="h-[36px] bg-red-500 hover:bg-red-600 col-span-1 text-white px-4 py-2 rounded-lg text-center text-sm">
                Delete
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

import './assets/main.css'
import 'primeicons/primeicons.css'
import toast from 'vue-toastification'
import 'vue-toastification/dist/index.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import PrimeVue from 'primevue/config';
import Aura from '@primevue/themes/aura';
import cors from 'cors'
import Dialog from "primevue/dialog";

const app = createApp(App);
app.use(router)
app.use(toast)
app.component('Dialog', Dialog);
app.use(cors)
app.mount('#app')

import AddView from '@/views/AddView.vue'
import HomeView from '@/views/HomeView.vue'
import ModifyView from '@/views/ModifyView.vue'
import NotFoundView from '@/views/NotFoundView.vue'
import TaskListView from '@/views/TaskListView.vue'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/tasks',
      name: 'tasks',
      component: TaskListView
    },
    {
      path: '/tasks/add',
      name: 'add',
      component: AddView
    },
    {
      path: '/tasks/update/:id',
      name: 'update',
      component: ModifyView
    },
    {
      path: '/:catchAll(.*)',
      name: 'not-found',
      component: NotFoundView
    },
  ]
})

export default router

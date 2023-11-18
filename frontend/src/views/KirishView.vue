<script>
import axios from 'axios'
import Toast from '@/components/Toast.vue'
import { useToastStore } from '@/stores/toast'
import { useUserStore } from '@/stores/user'
import { RouterLink } from 'vue-router'
import { defineComponent } from 'vue'
import { Carousel, Navigation, Slide } from 'vue3-carousel'
import 'vue3-carousel/dist/carousel.css'

export default defineComponent({
    setup() {
        const userStore = useUserStore()
        const toastStore = useToastStore()

        return {
            userStore,
            toastStore
        }
    },
    components: {
        Carousel,
        Slide,
        Navigation,
        Toast,
        RouterLink
    },

    data: () => ({
        posts: [],
        // carousel settings
        settings: {
            itemsToShow: 2,
            snapAlign: 'start',
        },
        // breakpoints are mobile first
        // any settings not specified will fallback to the carousel settings
        breakpoints: {
            // 700px and up
            700: {
                itemsToShow: 3,
                snapAlign: 'start',
            },
            // 1024 and up
            1024: {
                itemsToShow: 5,
                snapAlign: 'start',
            },
        },
    }),


    mounted() {
        this.getFeed()
    },

    methods: {
        getFeed() {
            axios
                .get('/api/courses/')
                .then(response => {
                    console.log('data', response.data)

                    this.posts = response.data
                })
                .catch(error => {
                    console.log('error', error)
                })
        },
    }
})
</script>

<template>
    <template v-if="userStore.user.isAuthenticated && userStore.user.id">
        <!-- <Carousel :wrapAround="true" :transition="700" v-bind="settings" :breakpoints="breakpoints">
            <Slide v-for="post in posts" :key="post" class="p-2">
                <div class="max-w-sm p-3 bg-slate-200 border border-gray-200 rounded-lg shadow">
                    <RouterLink :to="{ name: 'coursedetail', params: { id: post.id } }">
                        <p class="text-ls font-semibold tracking-tight text-gray-900 dark:text-white">
                            {{ post.name }}
                            <span
                                class="bg-green-300 text-blue-800 text-xs font-medium mr-2 px-2.5 py-1 rounded-full dark:bg-blue-900 dark:text-blue-300">
                                {{ post.workers.length }}
                            </span>
                        </p>
                    </RouterLink>
                </div>
            </Slide>

            <template #addons>
                <Navigation />
            </template>
        </Carousel> -->

        <div class="rounded-lgh-96 mb-4 p-5">
            <div class="bg-gray-100 shadow-xl relative sm:rounded-lg overflow-hidden">
                <div class="overflow-x-auto">
                    <table class="w-full text-sm text-left text-gray-500">
                        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700">
                            <tr>
                                <th scope="col" class="px-4 py-3">Guruhlar</th>
                                <th scope="col" class="px-4 py-3">Talabalar</th>
                                <th scope="col" class="px-4 py-3">Kunlar</th>
                                <th scope="col" class="px-4 py-3">Narx (so'm)</th>
                                <th scope="col" class="px-4 py-3">
                                    <span class="sr-only">Actions</span>
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="post in posts" :key="post" class="border-b dark:border-gray-700">
                                <th scope="row"
                                    class="px-4 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                                    <RouterLink :to="{ name: 'coursedetail', params: { id: post.id } }">
                                        {{ post.name }}
                                    </RouterLink>
                                </th>
                                <td class="px-4 py-3">
                                    <span
                                        class="px-3 py-1 text-xs font-medium leading-none text-center text-blue-800 bg-blue-200 rounded-full">
                                        {{ post.workers.length }}
                                    </span>
                                </td>
                                <td class="px-4 py-3">
                                    {{ post.status }}
                                </td>
                                <td class="px-4 py-3">
                                    {{ post.price }}
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </template>
    <template v-else>
        <p class="mt-10 text-center text-sm text-gray-900 dark:text-white">
            Please
            <RouterLink to="login" class="font-semibold leading-6 text-indigo-600 hover:text-indigo-700">
                Login
            </RouterLink>
        </p>
    </template>
</template>

<script>
import axios from 'axios'
import { RouterLink } from 'vue-router'

export default {

    data() {
        return {
            video: [],
            video_access: true,
            errors: [],
            add_access: '',
        }
    },

    mounted() {
        this.getFeed()
    },

    methods: {
        getFeed() {
            const config = {
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Authorization': `JWT ${localStorage.getItem('user.access')}`,
                }
            };
            axios
                .get(`/api/videos/video/${this.$route.params.id}/`, config)
                .then(response => {
                    console.log(response.data)
                    this.video = response.data['video']
                    this.video_access = false

                })
                .catch(error => {
                })
        },
        async AddAccess(id) {
            if ((localStorage.getItem('user.access'))) {
                const config = {
                    headers: {
                        'Authorization': `JWT ${localStorage.getItem('user.access')}`,
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                    }
                };
                const video_id = id;
                const body = JSON.stringify({
                    video_id
                });
                axios
                    .post(`/api/videos/video-mark/${this.$route.params.id}/`, body, config)
                    .then(response => {
                        if (response.status === 202) {
                            this.add_access = response.data['data']
                        }
                    })
                    .catch(error => {
                    })
            } else {
                this.toastStore.showToast(3000, "Please, Log In", 'Unauthorized', 'bg-red-500 text-white');
            }
        },
    }
}
</script>

<template>
    <template v-if="video_access">
        <div class="pr-2 pb-2">
            <div class="py-3 px-1 mx-1 w-full">
                <div class="pt-6 px-5">
                    <div role="status" class="space-y-8 animate-pulse md:space-y-0 md:space-x-8 md:flex md:items-center">
                        <div
                            class="flex items-center justify-center w-full h-48 bg-gray-300 rounded sm:w-96 dark:bg-gray-700">
                            <p>Video not access</p>
                        </div>
                        <span class="sr-only">Loading...</span>
                    </div>
                </div>
            </div>
        </div>
    </template>
    <template v-else>
        <div class="pr-2 pb-2">
            <div class="py-3 px-1 mx-1 w-full">
                <div class="pt-6">
                    <nav aria-label="Breadcrumb">
                        <ol role="list"
                            class="mx-auto flex max-w-2xl items-center space-x-2 px-4 sm:px-6 lg:max-w-7xl lg:px-8">
                            <div class="flex items-center">
                                <p class="mr-2 text-sm font-medium text-gray-600">
                                    Modul:{{ video.modul['name'] }}
                                </p>
                            </div>
                        </ol>
                    </nav>
                    <!-- Product info -->
                    <div
                        class="mx-auto max-w-2xl px-4 pb-16 pt-10 sm:px-6 lg:grid lg:max-w-7xl lg:grid-cols-3 lg:grid-rows-[auto,auto,1fr] lg:gap-x-8 lg:px-8 lg:pb-24 lg:pt-16">
                        <div class="lg:col-span-2 lg:border-r lg:border-gray-200 lg:pr-8">
                            <h1 class="text-2xl font-bold tracking-tight text-gray-900 sm:text-3xl">
                                {{ video.name }}
                            </h1>
                            <p>
                                {{ video.description }}
                            </p>
                        </div>
                        <!-- Options -->
                        <div class="mt-4 lg:row-span-3 lg:mt-0">
                            <div class="aspect-h-2 mb-6 aspect-w-3 overflow-hidden rounded-lg">

                                <video class="w-96" controls>
                                    <source :src="video.get_thumbnail" type="video/mp4">
                                    Your browser does not support the video tag.
                                </video>

                            </div>
                            <h2 class="sr-only">Product information</h2>
                            <p @click="AddAccess(video.id)"
                                class="text-xl tracking-tight mb-1 text-gray-900 cursor-pointer">
                                <span
                                    class="bg-green-100 text-green-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded dark:bg-green-900 dark:text-green-300">
                                    Mark is view
                                </span>
                            </p>
                        </div>

                    </div>
                </div>
            </div>
        </div>
    </template>
</template>
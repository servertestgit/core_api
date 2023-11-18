<script>
import axios from 'axios'

import { useToastStore } from '@/stores/toast'

export default {
    setup() {
        const toastStore = useToastStore()

        return {
            toastStore
        }
    },

    data() {
        return {
            form: {
                email: '',
                name: '',
                password1: '',
                password2: ''
            },
            errors: [],
        }
    },

    methods: {
        submitForm() {
            this.errors = []

            if (this.form.email === '') {
                this.errors.push('Your e-mail is missing')
            }

            if (this.form.name === '') {
                this.errors.push('Your name is missing')
            }

            if (this.form.password1 === '') {
                this.errors.push('Your password is missing')
            }

            if (this.form.password1 !== this.form.password2) {
                this.errors.push('The password does not match')
            }

            if (this.errors.length === 0) {
                axios
                    .post('/api/signup/', this.form)
                    .then(response => {
                        if (response.data.message === 'success') {
                            this.toastStore.showToast(5000, 'The user is registered. Please activate your account by clicking your email link.', 'Registration', 'bg-gradient-to-r from-[#b8bcf9] to-[#9992ff]')

                            this.form.email = ''
                            this.form.name = ''
                            this.form.password1 = ''
                            this.form.password2 = ''
                        } else {
                            const data = JSON.parse(response.data.message)
                            for (const key in data) {
                                this.errors.push(data[key][0].message)
                            }
                        }
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            }
        }
    }
}
</script>

<template>
    <div class="gap-16 items-center py-8 px-4 mx-auto max-w-screen-xl lg:grid lg:grid-cols-1 lg:py-16 lg:px-6">
        <div class="sm:mx-auto sm:w-full sm:max-w-sm" style="align-items: center;
                display: flex;
                flex-direction: column;
                justify-content: center;">
            <div>
                <h5 class="mb-3 text-base font-semibold text-dark md:text-xl">
                    Sign In
                </h5>
            </div>
            <div class="w-full p-4 bg-white border border-gray-200 rounded-lg shadow-2xl sm:p-6">
                <div class="sm:mx-auto sm:w-full sm:max-w-sm">
                    <div v-for="error in errors">
                        <div class="p-3 mb-2 text-xs text-red-800 rounded-lg bg-red-50 dark:bg-gray-800 dark:text-red-400"
                            role="alert">
                            <span class="font-medium">Error!</span> {{ error }}
                        </div>
                    </div>
                    <form class="space-y-6" v-on:submit.prevent="submitForm">
                        <div class="mb-2">
                            <label for="text" class="block mb-1 text-gray-900"
                                style="font-size: 0.6rem; line-height: 1rem;">
                                Full Name
                            </label>
                            <input type="text" v-model="form.name" id="text"
                                class="bg-gray-50 border border-gray-200 text-gray-900 text-sm rounded-sm focus:ring-blue-500 focus:border-blue-500 block w-full p-1.5"
                                required>
                        </div>
                        <div class="mb-2">
                            <label for="email" class="block mb-1 text-gray-900"
                                style="font-size: 0.6rem; line-height: 1rem;">
                                Email
                            </label>
                            <input type="email" v-model="form.email" id="email"
                                class="bg-gray-50 border border-gray-200 text-gray-900 text-sm rounded-sm focus:ring-blue-500 focus:border-blue-500 block w-full p-1.5"
                                required>
                        </div>
                        <div class="mb-2">
                            <label for="password" class="block mb-1 text-gray-900"
                                style="font-size: 0.6rem; line-height: 1rem;">
                                Password
                            </label>
                            <input type="password" id="password" v-model="form.password1"
                                class="bg-gray-50 border border-gray-200 text-gray-900 text-sm rounded-sm focus:ring-blue-500 focus:border-blue-500 block w-full p-1.5"
                                required>
                        </div>
                        <div class="mb-2">
                            <label for="password" class="block mb-1 text-gray-900"
                                style="font-size: 0.6rem; line-height: 1rem;">
                                Confirm Password
                            </label>
                            <input type="password" v-model="form.password2" id="password"
                                class="bg-gray-50 border border-gray-200 text-gray-900 text-sm rounded-sm focus:ring-blue-500 focus:border-blue-500 block w-full p-1.5"
                                required>
                        </div>
                        <button type="submit"
                            class="text-white bg-red-400 hover:bg-red-600 font-medium rounded-3xl text-sm w-full px-2 py-2 text-center">Submit</button>
                    </form>
                </div>
            </div>
            <div>
                <p class="mt-2 text-xs text-dark">
                    Already have an account?
                    <RouterLink to="login" class="font-semibold leading-6 text-indigo-600">
                        Sign In
                    </RouterLink>
                </p>
            </div>
        </div>
    </div>
</template>

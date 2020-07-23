<template>
    <div>
        <router-link to="/">&lt;- back</router-link>
        <div v-if="person">
            <h2>{{ person.name }} #{{ person.id }}</h2>
            <p>Status: <Status :status="person.status"></Status></p>
        </div>
    </div>
</template>
<script>
import Status from '../Status.vue';

export default {
    name: 'User',

    data() {
        return {
            person: null
        }
    },

    async mounted() {
        const response = await fetch(`/api/people/${this.$route.params.id}`)
        const person = await response.json();
        if (!person) {
            this.$router.push('/not-found')
        } else {
            this.person = person
        }
    },

    components: {
        Status
    }
}
</script>
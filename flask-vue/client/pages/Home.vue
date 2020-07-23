<template>
    <div>
        <p>This table data is loaded through a fetch call to the flask backend!</p>
        <b-table hover :items="people" :fields="fields">
            <template v-slot:cell(nameLink)="data">
                <router-link :to="`/user/${data.item.id}`">{{ data.item.name }}</router-link>
            </template>
        </b-table>
    </div>
</template>
<script>
export default {
    name: 'Home',

    components: {
    },

    data() {
        return {
            fields: [
                {
                    key: 'id',
                    label: '#'
                }, 
                {
                    key: 'nameLink',
                    label: 'Name'
                }, 
                {
                    key: 'status',
                    label: 'Status'
                }
            ],
            people: []
        }
    },

    async mounted() {
        const response = await fetch('/api/people');
        this.people = await response.json();
    }
}
</script>
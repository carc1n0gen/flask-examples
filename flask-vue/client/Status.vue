<template>
<span class="person-status">
    <span :class="['indicator', status.toLowerCase()]">{{ status.toUpperCase() }}</span>
</span>
</template>
<script>
export default {
    name: 'Status',

    props: ['status'],

    components: {
    }
}
</script>
<style lang="scss" scoped>
.person-status {
    .indicator {
        padding: 5px;
        border-radius: 4px;
    }

    .active {
        background-color: green;
        color: #Fff;
    }

    .inactive {
        background-color: red;
        color: #fff;
    }
}
</style>
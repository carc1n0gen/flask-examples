<template>
  <b-navbar toggleable="lg" type="light" variant="light">
    <b-navbar-brand to="/">Flask Vue</b-navbar-brand>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
    <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav active="/">
            <b-nav-item to="/" v-bind:active="$route.path === '/'">Home</b-nav-item>
            <b-nav-item to="/about" v-bind:active="$route.path === '/about'">About</b-nav-item>
        </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>
<script>
export default {
  name: 'Nav',

  components: {
  },
}
</script>

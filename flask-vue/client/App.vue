<template>
  <div>
    <Nav></Nav>
    <b-container>
      <router-view></router-view>
    </b-container>
  </div>
</template>
<script>
import Nav from './Nav.vue';

export default {
  name: 'App',
  components: {
    Nav
  }
}
</script>

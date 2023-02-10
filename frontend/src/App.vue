<template>
  <RouterView/>
</template>

<script>
  import NavBar from './components/NavBar.vue';

  export default{
    data(){
      return{
      }
    },
    components: { 
      NavBar,
    },
  }
</script>
  
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
nav li.router-link-exact-active {
  color: #42b983;

}
</style>

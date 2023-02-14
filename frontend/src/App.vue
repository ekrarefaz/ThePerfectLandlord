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
<<<<<<< HEAD

    setup() {
    return { sidebarWidth }
    }

    // beforeCreate(){
    //   this.$store.commit('initializeStore')
    //   if(this.$store.state.token){
    //     axios.defaults.header.common['Authorization'] = "Token" + this.$store.state.token
    //   }
    //   else{
    //     axios.defaults.header.common['Authorization'] = ""
    //   }
    // }
=======
>>>>>>> 79bc66c12efa5a81f414c7f84d087ba25064fc0b
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

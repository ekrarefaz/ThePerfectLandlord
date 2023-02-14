<template>
    <NavBar/>
    <LoginForm/>
</template>

<script>
import NavBar from '@/components/NavBar.vue';
import LoginForm from '../../components/LoginForm.vue'
    export default{
        data(){
            return{

            }
        },
        components:{
    LoginForm,
    NavBar
}
             
    }
</script>

<style>

</style>
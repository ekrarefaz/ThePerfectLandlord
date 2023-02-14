<template>
    <div class="login-box">
        <h2>Login</h2>
        <form @submit.prevent="authenticate">
          <div class="user-box">
<<<<<<< HEAD
            <input type="text" name="username" v-model="username" required="">
=======
            <input type="text" name="username" required="" v-model="username">
>>>>>>> 79bc66c12efa5a81f414c7f84d087ba25064fc0b
            <label>Username</label>
            <p>{{username}}</p>
          </div>
          <div class="user-box">
<<<<<<< HEAD
            <input type="password" name="password" v-model="password" required="">
            <label>Password</label>
          </div>
          <a href="#">
            <span></span>
            <span></span>
            <span></span>
            <span></span>
          </a>
          <button type="submit">Submit</button>
=======
            <input type="password" name="password" required="" v-model="password">
            <label>Password</label>
          </div>
          <input type="submit" value="submit" class="submitBtn">
>>>>>>> 79bc66c12efa5a81f414c7f84d087ba25064fc0b
        </form>
      </div>
</template>

<script>
import axios from 'axios';

<<<<<<< HEAD

  export default{
    data(){
      return{
        username: "",
        password: ""
      }
    },
    methods:{
      authenticate(){
        axios.defaults.headers.common['Authorization'] = ''
        localStorage.removeItem('token')

        const formData = {
          username: this.username,
          password: this.password
        }

        axios
          .post('http://127.0.0.1:8000/auth/login')
          .then(response=>{
            const token = response.data.auth_token

            this.$store.commit('setToken', token)

            axios.defaults.headers.common['Authorization'] = 'Token' + token
            
            localStorage.setItem('token', token)

            this.$router.push('/')
          })
      }
    }
  }
=======
  export default{
    data(){
      return{
        isAuthenticated: false,
        username: '',
        password: '',
        users: []
      }
    },
    methods:{
      async authenticate(){
        axios.defaults.headers.common['Authorization'] = ''
        localStorage.removeItem('token')

        const formData={
          username : this.username,
          password: this.password
        }

        await axios
        .post('http://127.0.0.1:8000/auth/token/login',formData)
        .then(response=>{
          const token = response.data.auth_token
          this.$store.commit('setToken', token)
          axios.defaults.headers.common['Authorization'] = 'Token' + token
          localStorage.setItem('token', token)

          this.$router.push('/properties')
          console.log("done")
        })
        }
      },
    }
>>>>>>> 79bc66c12efa5a81f414c7f84d087ba25064fc0b
</script>

<style scoped > 
html {
    height: 100%;
  }
  body {
    margin:0;
    padding:0;          
    font-family: sans-serif;
    background: linear-gradient(#141e30, #243b55);
  }
  
  .login-box {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 700px;
    height: 400px;
    padding: 40px;
    transform: translate(-50%, -50%);
    background: rgba(0,0,0,.5);
    box-sizing: border-box;
    box-shadow: 0 15px 25px rgba(0,0,0,.6);
    border-radius: 10px;
  }
  
  .login-box h2 {
    margin: 0 0 30px;
    padding: 0;
    color: #fff;
    text-align: center;
  }
  
  .login-box .user-box {
    position: relative;
  }
  
  .login-box .user-box input {
    width: 100%;
    padding: 10px 0;
    font-size: 16px;
    color: #fff;
    margin-bottom: 30px;
    border: none;
    border-bottom: 1px solid #fff;
    outline: none;
    background: transparent;
  }
  .login-box .user-box label {
    position: absolute;
    top:0;
    left: 0;
    padding: 10px 0;
    font-size: 16px;
    color: #fff;
    pointer-events: none;
    transition: .5s;
  }
  
  .login-box .user-box input:focus ~ label,
  .login-box .user-box input:valid ~ label {
    top: -20px;
    left: 0;
    color: red;
    font-size: 12px;
  }
  
<<<<<<< HEAD
  .login-box form submitBtn {
=======
  .login-box form .submitBtn {
>>>>>>> 79bc66c12efa5a81f414c7f84d087ba25064fc0b
    position: relative;
    display: inline-block;
    padding: 10px 20px;
    color: black;
    font-size: 16px;
    text-decoration: none;
    text-transform: uppercase;
    overflow: hidden;
    transition: .5s;
    margin-top: 40px;
    letter-spacing: 4px
  }
  
  .login-box .submitBtn:hover {
    background: red;
    color: #fff;
    border-radius: 5px;
  }
  
  .login-box .submitBtn span {
    position: absolute;
    display: block;
  }
  
</style>
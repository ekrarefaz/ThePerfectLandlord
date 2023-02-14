<template>
  <body>
    <div class="login-box">
        <h2>Signup</h2>
        <form @submit.prevent="createUser">
          <div class="user-box">
            <input type="text" name="username" v-model="username" required="">
            <label>Username</label>
          </div>
          <div class="user-box">
            <input type="text" name="email" v-model="email" required="">
            <label>Email</label>
          </div>
          <div class="user-box">
            <input type="password" name="password" v-model="password" required="">
            <label>Password</label>
          </div>
<<<<<<< HEAD
          <button type="submit">Submit</button>
=======
          <a href="#">
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            Submit
          </a>
>>>>>>> 79bc66c12efa5a81f414c7f84d087ba25064fc0b
        </form>
      </div>
    </body>
</template>

<script>
<<<<<<< HEAD
  import axios from 'axios'
=======
>>>>>>> 79bc66c12efa5a81f414c7f84d087ba25064fc0b
  export default{
    data(){
      return{
        username: '',
<<<<<<< HEAD
        email: '',
        password: ''
      }
    },
    methods:{
      createUser(){
        const formData = {
          username: this.username,
          email: this.email,
          password: this.password
        }
        axios
          .post('http://127.0.0.1:8000/auth/users/', formData)
          .then(response => {
            console.log("Created User")
          })
          
      }
=======
        password: ''
      }
>>>>>>> 79bc66c12efa5a81f414c7f84d087ba25064fc0b
    }
  }
</script>

<style scoped> 
html {
    height: 100%;
  }
  body {
    margin:0;
    padding:0;
    font-family: sans-serif;
    background-size: 100% 100%;
    background-position: 0px 0px,0px 0px,0px 0px,0px 0px,0px 0px;
    background-image: repeating-linear-gradient(315deg, #00FFFF2E 92%, #073AFF00 100%),repeating-radial-gradient(75% 75% at 238% 218%, #00FFFF12 30%, #073AFF14 39%),radial-gradient(99% 99% at 109% 2%, #6D4D1BFF 13%, #073AFF00 100%),radial-gradient(99% 99% at 21% 78%, #220101FF 0%, #073AFF00 100%),radial-gradient(160% 154% at 711px -303px, #282623FF 0%, #073AFFFF 100%);
  }
  
  .login-box {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 700px;
    height: auto;
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
  
  .login-box form a {
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
  
  .login-box a:hover {
    background: red;
    color: #fff;
    border-radius: 5px;
  }
  
  .login-box a span {
    position: absolute;
    display: block;
  }
  
</style>
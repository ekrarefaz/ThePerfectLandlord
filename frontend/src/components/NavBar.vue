<template>
    
<nav class="navbar">
    <ul>
        <li>
        <router-link :to="{name: 'landing'}">Home</router-link>
        </li>
        <li>
        <router-link :to="{name: 'login'}">Login</router-link>
        </li>
        <li>
        <router-link :to="{name: 'signup'}">Signup</router-link>
        </li>
    </ul>
</nav> 
</template>

<style scoped>
.navbar{
    position: fixed;
    left: 0;
    top: 0;
    width: 100vw;
    z-index: 3;
    height: 100px;
}
.navbar a{
    color: var(--text-color);
    background-color: var(--primary-bg);
}
.navbar ul{
    display: flex;
    align-items: center;
}
.navbar ul li{
    padding: 20px;
    display: block;
}
.navbar ul li:hover,
.navbar ul li:focus {
  border-color: rgba(0, 0, 0, 0.15);
  box-shadow: rgba(0, 0, 0, 0.1) 0 4px 4px;
  color: white;
  background-color: grey;
}
button:hover {
  transform: translateY(-0.5px);
}
</style>
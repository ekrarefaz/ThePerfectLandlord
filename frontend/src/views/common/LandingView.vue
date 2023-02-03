<template>
  <div class="main">
    <div class="heading-container">
      <div class="first-heading">
        <h1>The</h1>
      </div>
      <div class="second-heading">
        <h1>Perfect</h1>
      </div>
      <div class="third-heading">
        <h1>Landlord</h1>
      </div>
    </div>

    <div class="page-direction">
      <div class="tenant-btn">
        <router-link to="/properties">
          <button>I'm Looking to Rent</button>
        </router-link>
      </div>
      <div class="landlord-btn">
        <router-link to="/tenants">
          <button>I'm Looking for Tenants</button>
        </router-link>
      </div>
    </div>

  </div>
</template>

<script>

export default {
    name: "LandingPage",
    data() {
        return {};
    },
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
*{
  box-sizing: border-box;
  margin: 0px;
  padding: 0px;
  width: 90%;
  height: 90%;
}
.blur {
  filter: blur(10px);
}
.main{
  display: flex;
}
h1{
  font-size: 10em;
  margin: 0;
  padding: 5px;
  z-index: 0;
}
.first-heading,.second-heading,.third-heading{
  text-align: left;
  margin-left: 100px;
}
.tenant-btn,.landlord-btn{
  padding: 100px;
}
.page-direction{
  background-color: transparent;
  outline: 0ch;
  border: 2px beige;
  padding-left: 300px;
  padding-top: 100px;
}
button{
  align-items: center;
  background-color: #FFFFFF;
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: .25rem;
  box-shadow: rgba(0, 0, 0, 0.02) 0 1px 3px 0;
  box-sizing: border-box;
  color: rgba(0, 0, 0, 0.85);
  cursor:pointer;
  display: inline-flex;
  font-size: 20px;
  font-weight: 600;
  justify-content: center;
  line-height: 1.25;
  margin: 0;
  min-height: 3rem;
  padding: calc(.875rem - 1px) calc(1.5rem - 1px);
  position: relative;
  text-decoration: none;
  transition: all 250ms;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  vertical-align: baseline;
  width: auto;
}
button:hover,
button:focus {
  border-color: rgba(0, 0, 0, 0.15);
  box-shadow: rgba(0, 0, 0, 0.1) 0 4px 12px;
  color: white;
  background-color: black;
}
button:hover {
  transform: translateY(-1px);
}
button:active {
  background-color: #F0F0F1;
  border-color: rgba(0, 0, 0, 0.15);
  box-shadow: rgba(0, 0, 0, 0.06) 0 2px 4px;
  color: rgba(0, 0, 0, 0.65);
  transform: translateY(0);
}
</style>

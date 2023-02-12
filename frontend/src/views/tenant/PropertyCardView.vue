<template>
  <NavBar/>
      <div class="property-card-container">
        <div v-for="property in properties" :key="property.property_id">
          <router-link :to="{name: 'property-details', params: { id: property.property_id}}">
            <div class="property-card">
              <img src="../../assets/sample.jpg" alt="">
              <div class="property-card__body">
                  <span class="tag">
                  <p>{{property.bedrooms}} Bed {{property.bathrooms}} Bath</p>
                  </span>
                  <h1>{{property.address}}</h1>
                  <span class="price">{{property.weekly_price}}$/week</span>
                  <p class="description">
                      {{ property.desc }}
                  </p>
                  <button class="btn">
                      Details
                  </button>
              </div>
            </div>
          </router-link>
        </div>
      </div>
</template>

<script>
  import NavBar from '@/components/NavBar.vue';
  import axios from 'axios'

      export default{
      data() {
          return {
              properties: []
          };
      },

      methods: {
        async getData(){
          try{
            const response = await this.$http.get('http://127.0.0.1:8000/api/properties/')
            this.properties = response.data

          }
          catch(error){
            console.log(error)
          }
        }
      },
      created(){
        this.getData()
      },
      components: { NavBar }
  }
</script>

<style scoped>
*{
  box-sizing: border-box;
  margin: 0px;
  padding: 10px;
  text-decoration: none;
}
  .property-card-container {
    display:flex;
    flex-wrap: wrap;
    justify-content: space-evenly;
    align-items: center;
    width: 100%;
  }
  .property-card {
    background: white;
    flex: 1;
    border-radius: 15px;
    box-shadow: 1px 1px 50px rgba(0, 0, 0, 0.1);
    max-width: 700px;
    padding: 30px;
    width: 100vw;
    transition: ease-in .5s;

  }

  .property-card:hover{
    background: linear-gradient(270deg, beige, #3995a2);
    background-size: 400% 400%;

    -webkit-animation: glow 31s ease infinite;
    -moz-animation: glow 31s ease infinite;
    animation: glow 31s ease infinite;
  }

  @-webkit-keyframes glow {
    0%{background-position:0% 50%}
    50%{background-position:100% 50%}
    100%{background-position:0% 50%}
  }
  @-moz-keyframes glow {
    0%{background-position:0% 50%}
    50%{background-position:100% 50%}
    100%{background-position:0% 50%}
  }
  @keyframes glow {
    0%{background-position:0% 50%}
    50%{background-position:100% 50%}
    100%{background-position:0% 50%}
    }
  
  .property-card img {
    max-height: 150px;
  }
  .property-card .property-card__body h1 {
    margin-bottom: 15px;
  }
  .property-card .property-card__body .price {
    font-size: 18px;
    text-decoration: none;
  }
  .property-card .property-card__body .discount {
    font-size: 24px;
    font-weight: bold;
  }
  .property-card .property-card__body .description {
    margin-top: 15px;
    color: #303030;
  }
  .tag p {
    background: black;
    color: white;
    display: inline-block;
    padding: 3px 10px;
    border-radius: 50px;
    margin-bottom: 15px;
  }
  .property-card__body .btn {
    background: #168fe0;
    border: none;
    padding: 10px 20px;
    outline: none;
    border-radius: 5px;
    color: white;
    margin-top: 20px;
    width: 100%;
    box-shadow: 1px 4px 0px rgba(22, 143, 224, 0.5);
    transition: all 200ms ease-in-out;
    cursor: pointer;
  }
  .property-card__body .btn:hover {
    box-shadow: 0px 2px 0px rgba(22, 143, 224, 0.5);
  }
</style>
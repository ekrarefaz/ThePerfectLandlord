<template>
    <div v-for="property in properties" :key="property.id">
        div.main    
        <div class="property-card-container">
            <div class="property-card">
            <img src="../../assets/sample.jpg" alt="">
            <div class="property-card__body">
                <span class="tag">
                <p>{{property.bedrooms}} Bed {{property.bathrooms}} Bath</p>
                </span>
                <h1>{{property.address}}</h1>
                <span class="price">{{property.price}}$/week</span>
                <p class="description">
                    {{ property.description }}
                </p>
                <button class="btn">
                    Details
                </button>
            </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default{
        data(){
            return{
                properties: []
            }
        },
        mounted(){
            fetch('http://localhost:3000/properties')
            .then(res => res.json())
            .then(data => this.properties = data)
            .catch(err => console.log(err.message))
        }
    }
</script>

<style>
* {
    padding: 0;
    margin: 0;
  }
  .property-card-container {
    background: aliceblue;
    width: 100%;
    height: 210px;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-evenly;
  }
  .property-card {
    background: white;
    display: flex;
    border-radius: 15px;
    box-shadow: 1px 1px 50px rgba(0, 0, 0, 0.1);
    max-width: 700px;
    padding: 30px;
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
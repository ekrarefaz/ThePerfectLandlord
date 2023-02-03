<template>
    <h2>Properties Available for Rent</h2>
    <div class="property-main">
        <div class="property-container">
            <div v-for="property in properties" :key="property.id">
                <router-link :to="{name: 'property-details', params: {id: property.id}}">
                <div class="property">
                    <div class="image">
                        <img src="../../assets/sample.jpg" alt="">
                    </div>
                    <div class="details">
                        <h3>{{property.address}}</h3>
                        <p>{{property.bedrooms}}Bed, {{property.bathrooms}}Bath</p>
                        <span class="price-tag">
                            <h4> {{property.price}}/Week</h4>
                        </span>
                    </div>
                </div>
                </router-link>
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

<style scoped>
*{
    text-decoration: none;
}
.property-container{
    display: flex;
    align-content: space-around;
    padding: 10px;
    width:max-content;
    height: max-content;
    text-decoration: none;
    flex: 0 0 192px;
}
.property{
    text-decoration: none;
    border: 2px solid black;
    padding: 10px;
    margin: 15px;
    display: flex;
    align-content: space-between;

}
.property:hover{
    background:whitesmoke;
    border-radius: 10px;
}
.property a{
    text-decoration: none;
}
.image,.details{
    padding: 5px;
    text-decoration: none;
}
img{
    width: 100px;
    height: 100px;
}
.price-tag{
    float: right;
}


</style>
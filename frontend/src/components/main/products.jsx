import API from "../../api/api";
import { useState , useEffect } from "react";
const Products = () => {
    const [products,setProducts] = useState([]);
    useEffect(()=>{
        const fetchData = async () => {
            try{
                const response =  await API.get("/product/");
                console.log(response.data);
                setProducts(response.data);
        }catch (error){}
        };fetchData();
    },[])
    return (
        <div className="products">
            products
        </div>
    )
};export default Products ;
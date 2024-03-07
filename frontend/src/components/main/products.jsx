import API from "../../api/api";
import { useState , useEffect } from "react";
import { useParams } from "react-router-dom";
import { toast ,ToastContainer } from "react-toastify";
import { Link } from "react-router-dom";
import "react-toastify/dist/ReactToastify.css";
import "../../static/main/products.css";
const Products = () => {
    const [products,setProducts] = useState([]);
    const {category} = useParams();
    const fetchProductsCategory = async () => {
        await API.get(`/product/c/${category}/`).then((response) => {
            setProducts(response.data.products)
        }).catch((error) => toast.error("something went wrong,please try later ."))
    }
    const fetchData = async () => {
        await API.get("/product/").then((response) => {
            setProducts(response.data)
        }).catch((error) => toast.error("something went wrong,please try later ."))
    };
    useEffect(()=>{
    if(category){
        fetchProductsCategory();
    }else{
        fetchData();
    }
    },[])
    return (
        <div className="content">
            <h2>Products</h2>
            <div className="products">
            {
                products && products.map((product)=> {
                    return (
                        <Link className="product" key={product.id}>
                            <img src={product.image} />
                            <h3>{product.name}</h3>
                        </Link>
                    )
                })
            }
            </div>
            <ToastContainer draggable />
        </div>
    )
};export default Products ;
import "../static/category/category.css";
import {toast ,ToastContainer } from "react-toastify";
import 'react-toastify/dist/ReactToastify.css';
import {useState,useEffect} from "react";
import { Link, Outlet } from "react-router-dom";
import API from "../api/api";
const Categorys = () => {
    const [categories,setCategories] = useState([]);
    const fetchData = async () => {
        try{
            const response = await API.get("/product/c/");
            setCategories(response.data);
        }catch(error){
            toast.error("connection error,please try later .")
        }
    };useEffect(()=>{
        fetchData();
    },[]);
    return ( 
        <div className="content">
            <h2>Category</h2>
            <div className="categories">
                {
                    categories.map((category) => {
                        return (
                            <Link to={`/category/${category.id}/`} className="category" key={category.id}>
                                <img src={category.image} />
                                <h3>{category.name}</h3>
                            </Link>
                        )
                    })
                }
            </div>
            <ToastContainer draggable />
            <Outlet />
        </div>
    )
};export default Categorys;
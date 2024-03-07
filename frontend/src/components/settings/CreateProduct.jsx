import { useState, useEffect } from "react";
import API from "../../api/api";
import { ToastContainer , toast } from "react-toastify";
import 'react-toastify/dist/ReactToastify.css';
const CreateProduct = ()  => {
    const [data,setData] = useState({});
    const [categorys,setCategorys] = useState([]);
    const form = new FormData();
    const fetchCategorys = async () => {
        const response = await API.get("/product/c/");
        setCategorys(response.data)
    };
    useEffect(()=>{
        fetchCategorys();
    },[])
    const submitHandeler = (e) => {
        e.preventDefault();
        console.log("submit handeler")
        try{
            const sendData = async () => {
                for(const key in data){
                    form.append(key,data[key]);
                }
                await API.post("/product/",form).then((response)=> {
                    if(response.status === 201){
                        toast.success(`'${data.name}'created successfuly`);
                        setData({});
                    }
                }).catch((error) => {
                    toast.error(Object.values(error.response.data)[0][0])
                })
            };sendData();
        }catch(error){
            toast.error("something went wrong,please try later ")
        }
    };
    return (
        <form className="form" onSubmit={submitHandeler}>
            <div className="form-group">
                <h3 className="form-group-title">add product</h3>
            </div>
            <div className="form-group">
                <input type="text" onChange={(e)=> {
                    setData({...data,name:e.target.value})
                }}
                       required
                       placeholder="name"
                       className="form-group-input" />
            </div>
            <div className="form-group">
                <input type="number" min="0"
                       onChange={(e) => setData({...data,price:e.target.value})}
                       placeholder="price"
                       className="form-group-input" />
            </div>
            <div className="form-group">
                <input type="file" required
                       onChange={(e)=> setData({...data,image:e.target.files[0]})}
                       className="form-group-input form-group-file" />
            </div>
            <div className="form-group">
                <select className="form-group-select" onChange={(e)=>setData({...data,category:e.target.value})}>
                    {
                        categorys.map((item)=>{
                            return <option key={item.id} value={item.id}>{item.name}</option>
                        })
                    }
                </select>
            </div>
            <div className="form-group">
                <textarea type="text"
                          onChange={(e)=> setData({...data,description:e.target.value})}
                          placeholder="description"
                          className="form-group-input"></textarea>
            </div>
            <div className="form-group">
                <button type="submit" className="form-group-button">submit</button>
            </div>
            <ToastContainer draggable />
        </form>
    )
};export default CreateProduct ;
import API from "../../api/api";
import {useState,useEffect} from "react";
const CreateCategory = () => {
    const formData = new FormData();
    const [name,setName] = useState("");
    const [file,setFile] = useState("");
    const submitHandeler = async (event) => {
        event.preventDefault();
        formData.append("name",name);
        formData.append("image",file);
        try{
            const response = await API.post("/product/c/",formData);
            console.log(response.data)
        }catch(error){
            console.log(error)
        }
    };
    return (
        <form className="form" onSubmit={submitHandeler}>
            <div className="form-group">
                <h2 className="form-group-title">create category</h2>
            </div>
            <div className="form-group">
                <input type="text" className="form-group-input" placeholder="name"
                 onChange={(e)=> setName(e.target.value)} required />
            </div>
            <div className="form-group">
                <input type="file" className="form-group-input form-group-file" 
                onChange={(e)=> setFile(e.target.files[0])} required />
            </div>
            <div className="form-group">
                <button type="submit" className="form-group-button">create</button>
            </div>
        </form>
    )
};export default CreateCategory;
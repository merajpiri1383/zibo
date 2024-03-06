import { useState, useEffect } from "react";
const CreateProduct = ()  => {
    const [name,setName] = useState();
    const [price,setPrice] = useState();
    const [file,setFile] = useState();
    const [category,setCategory] = useState();
    const [description,setDescription] = useState();
    const submitHandeler = (e) => {
        e.preventDefault();
        console.log("submit handeler")
    };
    return (
        <form className="form" onSubmit={submitHandeler}>
            <div className="form-group">
                <h3 className="form-group-title">add product</h3>
            </div>
            <div className="form-group">
                <input type="text" onChange={(e)=>setName(e.target.value)}
                       required
                       placeholder="name"
                       className="form-group-input" />
            </div>
            <div className="form-group">
                <input type="number" min="0"
                       onChange={(e) => setPrice(e.target.value)}
                       placeholder="price"
                       className="form-group-input" />
            </div>
            <div className="form-group">
                <input type="file" required
                       onChange={(e)=> setFile(e.target.files[0])}
                       className="form-group-input form-group-file" />
            </div>
            <div className="form-group">
                <input type="text"
                       onChange={(e) => setCategory(e.target.value)}
                       placeholder="category"
                       className="form-group-input" />
            </div>
            <div className="form-group">
                <textarea type="text"
                          onChange={(e)=> setDescription(e.target.value)}
                          placeholder="description"
                          className="form-group-input"></textarea>
            </div>
            <div className="form-group">
                <button type="submit" className="form-group-button">submit</button>
            </div>
        </form>
    )
};export default CreateProduct ;
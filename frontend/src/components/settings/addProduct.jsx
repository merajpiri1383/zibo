const AddProduct = ()  => {
    return (
        <form className="form">
            <div className="form-group">
                <h3 className="form-group-title">add product</h3>
            </div>
            <div className="form-group">
                <input type="text" placeholder="name" className="form-group-input" />
            </div>
            <div className="form-group">
                <input type="number" min="0" placeholder="price" className="form-group-input" />
            </div>
            <div className="form-group">
                <input type="file" className="form-group-input form-group-file" />
            </div>
            <div className="form-group">
                <input type="text" placeholder="category" className="form-group-input" />
            </div>
            <div className="form-group">
                <textarea type="text" placeholder="description" className="form-group-input"></textarea>
            </div>
            <div className="form-group">
                <button className="form-group-button">submit</button>
            </div>
        </form>
    )
};export default AddProduct ;
<a id="sample-package"></a>
# `sample_package`

Sample package for testing docstring to markdown conversion.

This package contains various Python constructs with different docstring formats
to test the python-docstring-markdown package.

Available modules:
    - core: Core functionality with Google-style docstrings
    - utils: Utility functions with ReST-style docstrings
    - models: Data models with Numpydoc-style docstrings

<a id="core"></a>
# `core`

Core functionality module using Google-style docstrings.

This module demonstrates Google-style docstrings with various Python constructs
including nested classes, methods, and functions.

<a id="core-dataprocessor"></a>
## `core.DataProcessor`

Main data processing class.

This class demonstrates nested class definitions and various method types.

<a id="core-dataprocessor-init"></a>
### `core.DataProcessor.__init__`

```python
def __init__(self, name: str, config: Optional[Dict[str, Any]]):
```

Initialize the DataProcessor.

**Args:**

- `name`: Name of the processor
- `config`: Optional configuration dictionary

<a id="core-dataprocessor-config"></a>
### `core.DataProcessor.Config`

Nested configuration class.

This demonstrates nested class documentation.

<a id="core-dataprocessor-config-init"></a>
#### `core.DataProcessor.Config.__init__`

```python
def __init__(self):
```

Initialize Config object.

<a id="core-dataprocessor-config-update"></a>
#### `core.DataProcessor.Config.update`

```python
def update(self, settings: Dict[str, Any]) -> None:
```

Update configuration settings.

**Args:**

- `settings`: Dictionary of settings to update

<a id="core-dataprocessor-process"></a>
### `core.DataProcessor.process`

```python
def process(self, data: List[Any]) -> List[Any]:
```

Process the input data.

**Args:**

- `data`: List of data items to process

**Returns:** Processed data items

**Raises:**

- `ValueError` (*ValueError*): If data is empty

<a id="core-dataprocessor-transform"></a>
### `core.DataProcessor._transform`

```python
def _transform(self, item: Any) -> Any:
```

Internal method to transform a single item.

**Args:**

- `item`: Item to transform

**Returns:** Transformed item

<a id="core-batch-process"></a>
## `core.batch_process`

```python
def batch_process(processor: DataProcessor, items: List[Any]) -> Dict[str, List[Any]]:
```

Batch process items using a DataProcessor.

This is a module-level function demonstrating Google-style docstrings.

**Args:**

- `processor`: DataProcessor instance to use
- `items`: List of items to process

**Returns:** (*Dictionary containing*) - 'processed': List of processed items
- 'errors': List of items that failed processing

<a id="models"></a>
# `models`

Models module using Numpydoc-style docstrings.

This module demonstrates Numpydoc-style docstrings with data model classes.

<a id="models-basemodel"></a>
## `models.BaseModel`

Base model class for all data models.

**Args:**

- `id` (*str*): Unique identifier for the model
- `created_at` (*datetime*): Timestamp when the model was created

<a id="models-basemodel-to-dict"></a>
### `models.BaseModel.to_dict`

```python
def to_dict(self) -> Dict[str, Any]:
```

Convert model to dictionary.

**Returns:** (*Dict[str, Any]*) Dictionary representation of the model

<a id="models-user"></a>
## `models.User`

User model representing system users.

**Args:**

- `id` (*str*): Unique identifier for the user
- `username` (*str*): User's username
- `email` (*str*): User's email address
- `active` (*bool*): Whether the user is active, by default True

<a id="models-user-init"></a>
### `models.User.__init__`

```python
def __init__(self, id: str, username: str, email: str, active: bool):
```

<a id="models-user-to-dict"></a>
### `models.User.to_dict`

```python
def to_dict(self) -> Dict[str, Any]:
```

Convert user to dictionary.

**Returns:** (*Dict[str, Any]*) Dictionary containing all user fields

<a id="utils"></a>
# `utils`

Utility functions module using ReST-style docstrings.

This module demonstrates ReST-style docstrings with various utility functions.

<a id="utils-load-json"></a>
## `utils.load_json`

```python
def load_json(filepath: str) -> Dict[str, Any]:
```

Load and parse a JSON file.

**Args:**

- `filepath` (*str*): Path to the JSON file

**Returns:** (*dict*) Parsed JSON content as a dictionary

**Raises:**

- `FileNotFoundError` (*FileNotFoundError*): If the file doesn't exist
- `json.JSONDecodeError` (*json.JSONDecodeError*): If the file contains invalid JSON

<a id="utils-validate-data"></a>
## `utils.validate_data`

```python
def validate_data(data: Any, schema: Dict[str, Any]) -> List[str]:
```

Validate data against a schema.

This function demonstrates multi-paragraph ReST docstrings.

The schema should be a dictionary defining the expected structure
and types of the data.

**Args:**

- `data`: Data to validate
- `schema`: Schema to validate against

**Returns:** List of validation errors, empty if valid

<a id="utils-validationerror"></a>
## `utils.ValidationError`

Custom exception for validation errors.

**Args:**

- `message`: Error message
- `errors`: List of specific validation errors
Example::

    raise ValidationError("Invalid data", ["field1 is required"])

<a id="utils-validationerror-init"></a>
### `utils.ValidationError.__init__`

```python
def __init__(self, message: str, errors: List[str]):
```

Initialize ValidationError.

**Args:**

- `message`: Error message
- `errors`: List of validation errors

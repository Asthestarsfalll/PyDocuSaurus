# Documentation

## Table of Contents

- [`sample_package`](#sample-package)
  - [`core`](#sample-package-core)
    - [`DataProcessor`](#sample-package-core-dataprocessor)
      - [`__init__`](#sample-package-core-dataprocessor-init)
      - [`Config`](#sample-package-core-dataprocessor-config)
        - [`__init__`](#sample-package-core-dataprocessor-config-init)
        - [`update`](#sample-package-core-dataprocessor-config-update)
      - [`process`](#sample-package-core-dataprocessor-process)
      - [`_transform`](#sample-package-core-dataprocessor-transform)
    - [`batch_process`](#sample-package-core-batch-process)
  - [`models`](#sample-package-models)
    - [`BaseModel`](#sample-package-models-basemodel)
      - [`to_dict`](#sample-package-models-basemodel-to-dict)
    - [`User`](#sample-package-models-user)
      - [`__init__`](#sample-package-models-user-init)
      - [`to_dict`](#sample-package-models-user-to-dict)
  - [`utils`](#sample-package-utils)
    - [`load_json`](#sample-package-utils-load-json)
    - [`validate_data`](#sample-package-utils-validate-data)
    - [`ValidationError`](#sample-package-utils-validationerror)
      - [`__init__`](#sample-package-utils-validationerror-init)
  - [`exotic`](#sample-package-exotic)
    - [`advanced_types`](#sample-package-exotic-advanced-types)
      - [`Serializable`](#sample-package-exotic-advanced-types-serializable)
        - [`__init__`](#sample-package-exotic-advanced-types-serializable-init)
        - [`serialize`](#sample-package-exotic-advanced-types-serializable-serialize)
    - [`descriptors`](#sample-package-exotic-descriptors)
      - [`ValidatedField`](#sample-package-exotic-descriptors-validatedfield)
        - [`__init__`](#sample-package-exotic-descriptors-validatedfield-init)
        - [`__get__`](#sample-package-exotic-descriptors-validatedfield-get)
        - [`__set__`](#sample-package-exotic-descriptors-validatedfield-set)
    - [`protocols`](#sample-package-exotic-protocols)
      - [`Loggable`](#sample-package-exotic-protocols-loggable)
        - [`log_format`](#sample-package-exotic-protocols-loggable-log-format)
    - [`deep`](#sample-package-exotic-deep)
      - [`recursive`](#sample-package-exotic-deep-recursive)
        - [`Serializable`](#sample-package-exotic-deep-recursive-serializable)
          - [`__init__`](#sample-package-exotic-deep-recursive-serializable-init)
          - [`serialize`](#sample-package-exotic-deep-recursive-serializable-serialize)

<a id="sample-package"></a>
# `sample_package`

Sample package for testing docstring to markdown conversion.

This package contains various Python constructs with different docstring formats
to test the python-docstring-markdown package.

Available modules:
    - core: Core functionality with Google-style docstrings
    - utils: Utility functions with ReST-style docstrings
    - models: Data models with Numpydoc-style docstrings

<a id="sample-package-core"></a>
## `core`

Core functionality module using Google-style docstrings.

This module demonstrates Google-style docstrings with various Python constructs
including nested classes, methods, and functions.

<a id="sample-package-core-dataprocessor"></a>
### `DataProcessor`

Main data processing class.

This class demonstrates nested class definitions and various method types.

<a id="sample-package-core-dataprocessor-init"></a>
#### `__init__`

```python
def __init__(self, name: str, config: Optional[Dict[str, Any]]):
```

Initialize the DataProcessor.

**Args:**

- `name`: Name of the processor
- `config`: Optional configuration dictionary

<a id="sample-package-core-dataprocessor-config"></a>
#### `Config`

Nested configuration class.

This demonstrates nested class documentation.

<a id="sample-package-core-dataprocessor-config-init"></a>
##### `__init__`

```python
def __init__(self):
```

Initialize Config object.

<a id="sample-package-core-dataprocessor-config-update"></a>
##### `update`

```python
def update(self, settings: Dict[str, Any]) -> None:
```

Update configuration settings.

**Args:**

- `settings`: Dictionary of settings to update

<a id="sample-package-core-dataprocessor-process"></a>
#### `process`

```python
def process(self, data: List[Any]) -> List[Any]:
```

Process the input data.

**Args:**

- `data`: List of data items to process

**Returns:** Processed data items

**Raises:**

- (*ValueError*) If data is empty

<a id="sample-package-core-dataprocessor-transform"></a>
#### `_transform`

```python
def _transform(self, item: Any) -> Any:
```

Internal method to transform a single item.

**Args:**

- `item`: Item to transform

**Returns:** Transformed item

<a id="sample-package-core-batch-process"></a>
### `batch_process`

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

<a id="sample-package-models"></a>
## `models`

Models module using Numpydoc-style docstrings.

This module demonstrates Numpydoc-style docstrings with data model classes.

<a id="sample-package-models-basemodel"></a>
### `BaseModel`

Base model class for all data models.

**Args:**

- `id` (*str*): Unique identifier for the model
- `created_at` (*datetime*): Timestamp when the model was created

<a id="sample-package-models-basemodel-to-dict"></a>
#### `to_dict`

```python
def to_dict(self) -> Dict[str, Any]:
```

Convert model to dictionary.

**Returns:** (*Dict[str, Any]*) Dictionary representation of the model

<a id="sample-package-models-user"></a>
### `User`

User model representing system users.

**Args:**

- `id` (*str*): Unique identifier for the user
- `username` (*str*): User's username
- `email` (*str*): User's email address
- `active` (*bool*): Whether the user is active, by default True

<a id="sample-package-models-user-init"></a>
#### `__init__`

```python
def __init__(self, id: str, username: str, email: str, active: bool):
```

<a id="sample-package-models-user-to-dict"></a>
#### `to_dict`

```python
def to_dict(self) -> Dict[str, Any]:
```

Convert user to dictionary.

**Returns:** (*Dict[str, Any]*) Dictionary containing all user fields

<a id="sample-package-utils"></a>
## `utils`

Utility functions module using ReST-style docstrings.

This module demonstrates ReST-style docstrings with various utility functions.

<a id="sample-package-utils-load-json"></a>
### `load_json`

```python
def load_json(filepath: str) -> Dict[str, Any]:
```

Load and parse a JSON file.

**Args:**

- `filepath` (*str*): Path to the JSON file

**Returns:** (*dict*) Parsed JSON content as a dictionary

**Raises:**

- (*FileNotFoundError*) If the file doesn't exist
- (*json.JSONDecodeError*) If the file contains invalid JSON

<a id="sample-package-utils-validate-data"></a>
### `validate_data`

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

<a id="sample-package-utils-validationerror"></a>
### `ValidationError`

Custom exception for validation errors.

**Args:**

- `message`: Error message
- `errors`: List of specific validation errors
Example::

    raise ValidationError("Invalid data", ["field1 is required"])

<a id="sample-package-utils-validationerror-init"></a>
#### `__init__`

```python
def __init__(self, message: str, errors: List[str]):
```

Initialize ValidationError.

**Args:**

- `message`: Error message
- `errors`: List of validation errors

<a id="sample-package-exotic"></a>
## `exotic`

Exotic module demonstrating advanced Python features and docstring styles.

This module showcases various Python features including:
    - Type hints with Protocol and TypeVar
    - Async functions and context managers
    - Descriptors and metaclasses
    - Mixed docstring styles (Google, ReST, and Numpydoc)

<a id="sample-package-exotic-advanced-types"></a>
### `advanced_types`

Advanced type hints and generic types demonstration.

This module uses various type hints and generic types to showcase
complex typing scenarios.

<a id="sample-package-exotic-advanced-types-serializable"></a>
### `Serializable`

A generic serializable container.

Type Parameters
--------------
T
    The type of value being stored

<a id="sample-package-exotic-advanced-types-serializable-init"></a>
#### `__init__`

```python
def __init__(self, value: T):
```

<a id="sample-package-exotic-advanced-types-serializable-serialize"></a>
#### `serialize`

```python
def serialize(self) -> dict:
```

Convert the container to a dictionary.

**Returns:** (*dict*) A dictionary containing the value and metadata

<a id="sample-package-exotic-descriptors"></a>
### `descriptors`

Descriptors and metaclasses demonstration.

This module shows how to use descriptors and metaclasses
with proper documentation.

<a id="sample-package-exotic-descriptors-validatedfield"></a>
### `ValidatedField`

A descriptor that validates its values.

**Args:**

- `validator` (*callable*): A function that takes a value and returns True if valid
- `error_message` (*str*): Message to display when validation fails

<a id="sample-package-exotic-descriptors-validatedfield-init"></a>
#### `__init__`

```python
def __init__(self, validator, error_message):
```

<a id="sample-package-exotic-descriptors-validatedfield-get"></a>
#### `__get__`

```python
def __get__(self, instance, owner):
```

Get the field value.

**Args:**

- `instance`: The instance being accessed
- `owner`: The owner class

**Returns:** The field value

<a id="sample-package-exotic-descriptors-validatedfield-set"></a>
#### `__set__`

```python
def __set__(self, instance, value):
```

Set and validate the field value.

**Args:**

- `instance`: The instance being modified
- `value`: The new value to set

**Raises:**

- (*ValueError*) If the value fails validation

<a id="sample-package-exotic-protocols"></a>
### `protocols`

Protocol and structural subtyping examples.

This module demonstrates the use of Protocol for structural subtyping
and abstract base classes.

<a id="sample-package-exotic-protocols-loggable"></a>
### `Loggable`

Protocol for objects that can be logged.

Args:
    None

Returns:
    str: A string representation suitable for logging

Example:
    >>> class MyClass(Loggable):
    ...     def log_format(self) -> str:
    ...         return "MyClass instance"

<a id="sample-package-exotic-protocols-loggable-log-format"></a>
#### `log_format`

```python
def log_format(self) -> str:
```

Format the object for logging.

**Returns:** A string representation of the object

<a id="sample-package-exotic-deep"></a>
### `deep`


<a id="sample-package-exotic-deep-recursive"></a>
#### `recursive`

A little recursive module using ReST-style docstrings.

This module demonstrates ReST-style docstrings with various utility functions.

<a id="sample-package-exotic-deep-recursive-serializable"></a>
### `Serializable`

<a id="sample-package-exotic-deep-recursive-serializable-init"></a>
#### `__init__`

```python
def __init__(self, data: Dict[str, Any]) -> None:
```

Initialize a Serializable object.

**Args:**

- `data`: Data to serialize

<a id="sample-package-exotic-deep-recursive-serializable-serialize"></a>
#### `serialize`

```python
def serialize(self) -> Dict[str, Any]:
```

Serialize the object to a dictionary.

**Returns:** (*Dict[str, Any]*) Dictionary representation of the object

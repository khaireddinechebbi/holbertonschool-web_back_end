export default class Currency {
  constructor(code, name) {
    if (typeof code !== 'string') {
      throw new TypeError('code must be a string');
    }
    this._code = code;

    if (typeof name !== 'string') {
      throw new TypeError('name must be a string');
    }
    this._name = name;
  }

  get code() {
    return this._code;
  }

  set code(newcode) {
    if (typeof code !== 'string') {
      throw new TypeError('code must be a string');
    }
    this._code = newcode;
  }

  get name() {
    return this._name;
  }

  set name(newname) {
    if (typeof newname !== 'string') {
      throw new TypeError('name must be a string');
    }
    this._name = newname;
  }
}

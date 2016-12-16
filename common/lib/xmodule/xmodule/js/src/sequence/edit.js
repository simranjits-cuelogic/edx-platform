/* globals XModule */
/* eslint-disable no-underscore-dangle */

(function() {
    'use strict';

    var __hasProp = {}.hasOwnProperty,
        __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; }; // eslint-disable-line

    this.SequenceDescriptor = (function(_super) {
        function SequenceDescriptor() {
            return SequenceDescriptor.__super__.constructor.apply(this, arguments);
        }

        __extends(SequenceDescriptor, _super);

        return SequenceDescriptor;
    }(XModule.Descriptor));
}).call(this);

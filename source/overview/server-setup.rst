Server Setup
==========================================

Telephone Bot is designed to work "out of the box". It does not explicitly *need* any initial setup process on a server. However, there are several aspects which may be customized on a per-server basis.


Automated announcements
------------------------------------------
If desired, automatic announcements for the map rotation, Grizzco shifts, and SplatNet2 may be toggled in the desired channel by using :ref:`.utility rotation-add`, :ref:`.utility grizzco-add`, or :ref:`.utility splatnet-add`, respectively.


Customizing the command prefix
------------------------------------------
If you wish to change the prefix, you can do so by using :ref:`.utility prefix` followed by the desired prefix. For example, ``.utility prefix !`` to make issuing bot commands be like ``!profile`` instead of the default ``.profile``.

.. tip::
	You can use the :ref:`quoted argument syntax <quoted arguments>` to create more unique command prefixes.
	
	For example, using ``.utility prefix ".tele "`` (note the space after "tele" that's also within the quotation marks) mill make command invocation be like ``.tele profile``.

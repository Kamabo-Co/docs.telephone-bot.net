``.profile`` — View and edit your profile
========================================================================

.profile
------------------------------------------
Displays your profile, or the profile of the specified user.

Usage: ``.profile [user]``


.profile userfc
------------------------------------------
Show the friend code of the specified user.

Example: :samp:`.profile userfc {Ran#0004}`


.profile create
------------------------------------------
Registers you in the database and creates a profile.


.profile ign
------------------------------------------
Set the Switch username displayed on your profile.

.. note::
	Switch rules apply here! You cannot have a username longer than 10 :term:`character`\ s on the Switch, and this command enforces that rule.

Example: :samp:`.profile ign {Squint-Eye}`


.profile fc
------------------------------------------
Set or display your Nintendo Switch friend code.

Usage: ``.profile fc [friend-code]``

.. versionadded:: 2.7
	Invoking without any parameters displays your friend code.


.profile level
------------------------------------------

Set the in-game level displayed on your profile.

.. note::
	Star-levels are supported: If you specify a level above 99, from 100 up to 198, it will be displayed accordingly on your profile as a star-level of ⭐1 to ⭐99. For example: ``.profile level 141`` will be displayed as level ⭐142.

Example: :samp:`.profile level {101}`

.. versionadded:: 2.7
	An asterisk can be prepended to a level of 1-99 in order to specify that it is a star-level.


.profile rank
------------------------------------------
Set the ranks displayed on your profile.

Usage: ``.profile rank <mode> <rank> [power]``

.. note::
	Rank X is fully supported: Just specify your rank as ``X`` followed by your power level.

Example: :samp:`.profile rank {clamblitz} {X 1500}`

.. versionchanged:: 2.7
	Non-integer (i.e. 2005.6) X-rank powers are now accepted.


.profile clan
------------------------------------------
Set your team/clan on your profile.

Usage: ``.profile clan <invite-link>``

Example: :samp:`.profile clan {https://discord.gg/ZCwQPwn}`

.. important::
	Specifying a complete invite link (:samp:`{https://discord.gg/}ZCwQPwn`) will display the team/clan server's name as a usable invite link. To *not* provide an invite link on your profile, only specify the invite code itself.

	For example: :samp:`.profile clan {ZCwQPwn}`


.profile title
------------------------------------------
Set the title displayed on your profile.

.. note::
	Except for the default title (``No``), you must own a title before you can display it on your profile.

	You can get additional s at random from :ref:`the vending machine <command metro vending-machine>`.

Usage: ``.profile title <title-name>``

Example: :samp:`.profile title {Agent}`


.. index::
	see: gender; style

.profile style
------------------------------------------
Set the player character displayed on your profile.

Usage: ``.profile style <keyword> [additional-keywords…]``

.. versionadded:: 2.8
	Keywords for hair styles and skin tones.


.profile banner
------------------------------------------
Change the banner displayed on your profile.

Usage: ``.profile banner <banner-name>``

.. note::
	With the exception of the default banner (``Octo-Expansion``), you must own the banner before you can display it on your profile.

	You can get additional s at random from :ref:`the vending machine <command metro vending-machine>`.

Example: :samp:`.profile banner {Octo-Expansion}`


.profile loadout
------------------------------------------
Set the gear shown on your profile.

Usage: ``.profile loadout <gear-type> <main-ability> <sub-slot-count> <gear-name>``

.. attention::
	This is by far the most difficult command to use. Take careful note of the order and purpose of each parameter. For example:

	:samp:`.profile loadout Headgear runspeedup 2 King Flip Mesh`

	The four parameters specify, in order:

	-	This will be setting the *headgear* on the profile.
	-	The *main ability* of this gear is :t:`Run Speed Up`.
	-	There are only *two sub-ability slots* unlocked on the gear.
	-	The gear item itself is the :t:`King Flip Mesh`.


.profile ability
------------------------------------------
Set the sub-abilities on your gear.

Usage: ``.profile ability <gear-type> <sub-ability> [sub-ability [sub-ability]]``

.. note::
	For example: ``.profile ability shoes bombdefenseup specialchargeup quickrespawn``


.profile splatfest
------------------------------------------
Declare your side in the upcoming or ongoing Splatfest.

Usage: ``.profile spatfest <team>``

.. note::
	This command in only available for a limited time, and automatically locks at the end of the Splatfest. On occasion, special commemorative items are distributed to the winning team.

Examples:

| :samp:`.profile spatfest {mushroom}`
| :samp:`.profile spatfest {star}`


.profile delete
------------------------------------------
Completely deletes your entire account and related data.

Usage: ``.profile delete [confirmation-code]``

When first invoked without any argument, the command generates a confirmation code, *which is valid for up to one minute*.

.. danger::
	This is irreversible and your **data can not be recovered** afterwards.

.. versionchanged:: 2.7.1
	Confirmation codes are valid for exactly one minute after being generated.
